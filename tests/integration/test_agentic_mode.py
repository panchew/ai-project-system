"""
Scenario 5: Agentic Mode Test
Verify that the daemon running in a background thread automatically monitors directories,
and routes completion notices, review decisions, and delivery notices correctly.
"""

import json
import time
import pytest
import threading
from pathlib import Path
from lib.daemon_extensions import daemon_artifact_monitoring_loop


def test_agentic_mode(
    tmp_project,
    make_completion_notice,
    make_review_decision,
    make_delivery_notice
):
    """Test background daemon automatic directory monitoring and routing."""
    
    # 1. Start daemon loop in a background thread with an aggressive 0.05s interval for maximum speed
    daemon_thread = threading.Thread(
        target=daemon_artifact_monitoring_loop,
        args=(tmp_project, 0.05),
        daemon=True,
    )
    daemon_thread.start()
    
    # Let the thread start
    time.sleep(0.1)
    
    # 2. Add Completion Notice to completion-notices/ folder
    cn_file = make_completion_notice(
        project=tmp_project,
        epic_id="P1-M14-E14.2",
        milestone_id="P1-M14",
        phase_id="P1",
        timestamp="2026-06-01T12:00:00Z"
    )
    
    # 3. Wait for background thread to detect, parse, route, and move the Completion Notice
    timeout = 2.0
    start_time = time.time()
    processed_cn = tmp_project / ".ai-project" / "artifacts" / "completion-notices" / ".processed" / cn_file.name
    cn_trigger = tmp_project / ".ai-project" / "queue" / "route_completion_P1-M14-E14.2.json"
    
    while time.time() - start_time < timeout:
        if processed_cn.exists() and cn_trigger.exists():
            break
        time.sleep(0.05)
        
    assert processed_cn.exists(), "Daemon did not process Completion Notice in time"
    assert cn_trigger.exists(), "Daemon did not generate trigger for Completion Notice"
    
    with open(cn_trigger, "r", encoding="utf-8") as f:
        cn_data = json.load(f)
        assert cn_data["parent"] == "milestone"
        assert cn_data["parent_ref"] == "P1-M14"
        assert cn_data["epic_id"] == "P1-M14-E14.2"

    # 4. Add Review Decision to review-decisions/ folder
    rd_file = make_review_decision(
        project=tmp_project,
        decision="accept",
        epic_id="P1-M14-E14.2",
        milestone_id="P1-M14",
        feedback="Accepted by daemon test",
        timestamp="2026-06-01T13:00:00Z",
        cn_timestamp="2026-06-01T12:00:00Z"
    )
    
    # 5. Wait for daemon to detect and route Review Decision
    start_time = time.time()
    processed_rd = tmp_project / ".ai-project" / "artifacts" / "review-decisions" / ".processed" / rd_file.name
    rd_trigger = tmp_project / ".ai-project" / "queue" / "route_review_P1-M14-E14.2.json"
    
    while time.time() - start_time < timeout:
        if processed_rd.exists() and rd_trigger.exists():
            break
        time.sleep(0.05)
        
    assert processed_rd.exists(), "Daemon did not process Review Decision in time"
    assert rd_trigger.exists(), "Daemon did not generate trigger for Review Decision"
    
    with open(rd_trigger, "r", encoding="utf-8") as f:
        rd_data = json.load(f)
        assert rd_data["target"] == "epic"
        assert rd_data["target_ref"] == "P1-M14-E14.2"
        assert rd_data["decision"] == "accept"

    # 6. Add Delivery Notice to delivery-notices/ folder
    dn_file = make_delivery_notice(
        project=tmp_project,
        epic_id="P1-M14-E14.2",
        milestone_id="P1-M14",
        timestamp="2026-06-01T13:15:00Z",
        cn_timestamp="2026-06-01T12:00:00Z",
        rd_timestamp="2026-06-01T13:00:00Z"
    )
    
    # 7. Wait for daemon to detect and route Delivery Notice
    start_time = time.time()
    processed_dn = tmp_project / ".ai-project" / "artifacts" / "delivery-notices" / ".processed" / dn_file.name
    dn_trigger = tmp_project / ".ai-project" / "queue" / "route_delivery_P1-M14-E14.2.json"
    
    while time.time() - start_time < timeout:
        if processed_dn.exists() and dn_trigger.exists():
            break
        time.sleep(0.05)
        
    assert processed_dn.exists(), "Daemon did not process Delivery Notice in time"
    assert dn_trigger.exists(), "Daemon did not generate trigger for Delivery Notice"
    
    with open(dn_trigger, "r", encoding="utf-8") as f:
        dn_data = json.load(f)
        assert dn_data["parent"] == "milestone"
        assert dn_data["parent_ref"] == "P1-M14"
        assert dn_data["epic_id"] == "P1-M14-E14.2"
        
    # Check that original files are archived and removed from source directories
    assert not cn_file.exists()
    assert not rd_file.exists()
    assert not dn_file.exists()

import subprocess
import os

def test_run_postman_collection():
    report_name = "postman_advanced_report.html"
    command = f'newman run "My Collection.postman_collection.json" -r "cli,htmlextra" --reporter-htmlextra-export {report_name}'
    
    print("\n[INFO] Python subprocess triggering Postman integration suite via Newman...")

    result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='utf-8')

    
    print(result.stdout)
    
    assert result.returncode == 0, f"Postman automation suite failed! Error: {result.stderr}"
    assert os.path.exists(report_name), "Dynamic HTML report generation failed!"
    print(f"[SUCCESS] Execution completed. Artifact generated at: {report_name}")
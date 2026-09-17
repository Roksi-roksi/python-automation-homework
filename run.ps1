$OutputEncoding = [System.Text.Encoding]::UTF8

$results = "./allure-results"
$report = "./final-report"
$rep_history = "$report/history"

if (Test-Path $results) {
    Remove-Item -Recurse -Force $results
}

python -m pytest lesson_10/ --alluredir=$results

if (Test-Path $rep_history) {
    New-Item -ItemType Directory -Force -Path "$results/history" | Out-Null
    Copy-Item -Path "$rep_history\*" -Destination "$results/history" -Force
}

if (Test-Path $report) {
    Get-ChildItem -Path $report -Exclude "history" | Remove-Item -Recurse -Force
}

allure generate $results -o $report --clean

allure open $report

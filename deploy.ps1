# Скрипт для отправки изменений в Git
# Выполните: .\deploy.ps1

Write-Host "=== Проверка статуса Git ===" -ForegroundColor Cyan
git status

Write-Host "`n=== Добавление всех изменений ===" -ForegroundColor Cyan
git add -A

Write-Host "`n=== Проверка добавленных файлов ===" -ForegroundColor Cyan
git status --short

Write-Host "`n=== Создание коммита ===" -ForegroundColor Cyan
git commit -m "Fix mobile layout: remove side padding, center content, fix box proportions and background alignment"

Write-Host "`n=== Проверка текущей ветки ===" -ForegroundColor Cyan
$branch = git branch --show-current
Write-Host "Текущая ветка: $branch" -ForegroundColor Yellow

Write-Host "`n=== Отправка изменений на сервер ===" -ForegroundColor Cyan
git push origin $branch

Write-Host "`n=== Готово! ===" -ForegroundColor Green


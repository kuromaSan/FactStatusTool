# DocumentObject

[ドキュメント](./Documents/README.md)

## 概要

shellスクリプトテンプレート

## 環境構築

※管理者権限で実行
### Bash
推奨 実行コマンド
```bash
sudo apt update && sudo apt install -y yq  # Debian/Ubuntu
sudo dnf install -y yq                     # Fedora
brew install yq                             # macOS (Homebrew)
```
確認コマンド
```bash
yq --version
# yq version 1.0.0
```
### PowerShell
推奨 実行コマンド
```powerShell
Install-Module -Name powershell-yaml -Force -Scope AllUsers
```
確認コマンド
```powerShell
Get-Module -ListAvailable powershell-yaml
# Directory: C:\Program Files\WindowsPowerShell\Modules\powershell-yaml
```
#pegando o diretório
$scriptDirectory = Split-Path -Path $MyInvocation.MyCommand.Definition -Parent

#arquivo de saída sql
$outputFile = Join-Path -Path $scriptDirectory -ChildPath "migration.sql"

#verificando existencia do arquivo, se houver deleta
if (Test-Path $outputFile){
    Remove-Item $outputFile
}

#pegando o conteudo dos arquivos
$sqlFiles = Get-ChildItem -Path $scriptDirectory -Filter *.sql -File | Sort-Object Name

#consolidando aquirvos
foreach ($file in $sqlFiles){
    Get-Content $file.FullName | Out-File -Append -FilePath $outputFile
    "GO" | Out-File -Append -FilePath $outputFile
}

#mensagem de sucesso
Write-Host "Todos Arquivos foram combinados no $outputFile"
#!/bin/bash
git config credential.helper store
git push https://github.com/byrozaurowe/akiso_aktualizacje_strony.git
links -dump $1 | cat > aktualn_wersja
git add aktualn_wersja
git commit -m "aktualizacja"
git push 
while [ true ] ; do
cat aktualn_wersja > poprz_wersja
links -dump $1 | cat > aktualn_wersja
git add aktualn_wersja
git commit -m "aktualizacja"
git push 
diff poprz_wersja aktualn_wersja
sleep $2
done
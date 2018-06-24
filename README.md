# ortools_shiftg

Google Optimization Toolsを使って１０人の従業員を制約条件に基づいて、一週間ずつ確認を取りながら学習してスケジュールを作っていくPythonプログラム

一週間ごとの出力をrejectでき、rejectした場合は従業員ごとにFeedback coefficientを更新していく


# **環境構築**
---
必要ライブラリのインストール(足りないのがあれば必要に応じてpip installしてください。)
```
$ pip install  -r requirements.txt
```  
# **初期制約**
---

- 10人の従業員、最適化は7日ずつ
- 平日は３人  土日は５人の従業員を配員  
- それぞれの従業員は週に4日以下2日以上勤務  
- id:0,1,2をマネージャーとして、平日一人、土日二人のマネージャーの勤務が必須  
- 月ごとに従業員の出勤希望、出勤可能、公休希望、出勤不可能を設定  




# **参考**
---

[nurse schedulig program]
[constrainted queen](https://developers.google.com/optimization/cp/queens)  
[mixed integer programming](https://developers.google.com/optimization/assignment/assignment_mip)  


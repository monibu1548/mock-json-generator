# mock-json-generator
* 찾다찾다 없어서 만든 파이썬 스크립트
* 형식, 변경될 값을 지정하면 모든 경우의 json mock을 만듭니다

## format.py
Object 껍데기를 선언합니다. python의 Object 이며, 변경될 key에는 "#" 을 변수 앞뒤로 붙여줍니다
ex)
``` python
format = """
{
    "type": "#type#",
    "name": "#name#",
    "age": "#age#",
    "fixed": "fixed", // 변경하지 않을 값은 그대로 넣어둡니다
    "male": "#male#"
}
"""
```

## variables.py
format.py에 정의한 변경 가능한 key들에 대해서 어떤 values를 가질 수 있는지 정의합니다.
ex)
```python
variables = {
    "type": ["student", "teacher", "doctor"], // string 사용 가능
    "name": [None, "peter", "jingyu"], // optional ( null ) 사용 가능
    "age": [8, 12, 20], // number 사용 가능
    "male": [True, False] // bool 사용 가능
}
```

## mapper.py
format.py, varialbes.py 를 이용해 모든 케이스를 조합, 출력합니다

실행: `./python3 mapper.py` 

결과:
```json
[{"type": "student", "name": null, "age": 8, "fixed": "fixed", "male": true}, {"type": "teacher", "name": null, "age": 8, "fixed": "fixed", "male": true}, {"type": "doctor", "name": null, "age": 8, "fixed": "fixed", "male": true}, {"type": "student", "name": "peter", "age": 8, "fixed": "fixed", "male": true}, {"type": "teacher", "name": "peter", "age": 8, "fixed": "fixed", "male": true}, {"type": "doctor", "name": "peter", "age": 8, "fixed": "fixed", "male": true}, {"type": "student", "name": "jingyu", "age": 8, "fixed": "fixed", "male": true}, {"type": "teacher", "name": "jingyu", "age": 8, "fixed": "fixed", "male": true}, {"type": "doctor", "name": "jingyu", "age": 8, "fixed": "fixed", "male": true}, {"type": "student", "name": null, "age": 12, "fixed": "fixed", "male": true}, {"type": "teacher", "name": null, "age": 12, "fixed": "fixed", "male": true}, {"type": "doctor", "name": null, "age": 12, "fixed": "fixed", "male": true}, {"type": "student", "name": "peter", "age": 12, "fixed": "fixed", "male": true}, {"type": "teacher", "name": "peter", "age": 12, "fixed": "fixed", "male": true}, {"type": "doctor", "name": "peter", "age": 12, "fixed": "fixed", "male": true}, {"type": "student", "name": "jingyu", "age": 12, "fixed": "fixed", "male": true}, {"type": "teacher", "name": "jingyu", "age": 12, "fixed": "fixed", "male": true}, {"type": "doctor", "name": "jingyu", "age": 12, "fixed": "fixed", "male": true}, {"type": "student", "name": null, "age": 20, "fixed": "fixed", "male": true}, {"type": "teacher", "name": null, "age": 20, "fixed": "fixed", "male": true}, {"type": "doctor", "name": null, "age": 20, "fixed": "fixed", "male": true}, {"type": "student", "name": "peter", "age": 20, "fixed": "fixed", "male": true}, {"type": "teacher", "name": "peter", "age": 20, "fixed": "fixed", "male": true}, {"type": "doctor", "name": "peter", "age": 20, "fixed": "fixed", "male": true}, {"type": "student", "name": "jingyu", "age": 20, "fixed": "fixed", "male": true}, {"type": "teacher", "name": "jingyu", "age": 20, "fixed": "fixed", "male": true}, {"type": "doctor", "name": "jingyu", "age": 20, "fixed": "fixed", "male": true}, {"type": "student", "name": null, "age": 8, "fixed": "fixed", "male": false}, {"type": "teacher", "name": null, "age": 8, "fixed": "fixed", "male": false}, {"type": "doctor", "name": null, "age": 8, "fixed": "fixed", "male": false}, {"type": "student", "name": "peter", "age": 8, "fixed": "fixed", "male": false}, {"type": "teacher", "name": "peter", "age": 8, "fixed": "fixed", "male": false}, {"type": "doctor", "name": "peter", "age": 8, "fixed": "fixed", "male": false}, {"type": "student", "name": "jingyu", "age": 8, "fixed": "fixed", "male": false}, {"type": "teacher", "name": "jingyu", "age": 8, "fixed": "fixed", "male": false}, {"type": "doctor", "name": "jingyu", "age": 8, "fixed": "fixed", "male": false}, {"type": "student", "name": null, "age": 12, "fixed": "fixed", "male": false}, {"type": "teacher", "name": null, "age": 12, "fixed": "fixed", "male": false}, {"type": "doctor", "name": null, "age": 12, "fixed": "fixed", "male": false}, {"type": "student", "name": "peter", "age": 12, "fixed": "fixed", "male": false}, {"type": "teacher", "name": "peter", "age": 12, "fixed": "fixed", "male": false}, {"type": "doctor", "name": "peter", "age": 12, "fixed": "fixed", "male": false}, {"type": "student", "name": "jingyu", "age": 12, "fixed": "fixed", "male": false}, {"type": "teacher", "name": "jingyu", "age": 12, "fixed": "fixed", "male": false}, {"type": "doctor", "name": "jingyu", "age": 12, "fixed": "fixed", "male": false}, {"type": "student", "name": null, "age": 20, "fixed": "fixed", "male": false}, {"type": "teacher", "name": null, "age": 20, "fixed": "fixed", "male": false}, {"type": "doctor", "name": null, "age": 20, "fixed": "fixed", "male": false}, {"type": "student", "name": "peter", "age": 20, "fixed": "fixed", "male": false}, {"type": "teacher", "name": "peter", "age": 20, "fixed": "fixed", "male": false}, {"type": "doctor", "name": "peter", "age": 20, "fixed": "fixed", "male": false}, {"type": "student", "name": "jingyu", "age": 20, "fixed": "fixed", "male": false}, {"type": "teacher", "name": "jingyu", "age": 20, "fixed": "fixed", "male": false}, {"type": "doctor", "name": "jingyu", "age": 20, "fixed": "fixed", "male": false}]
```


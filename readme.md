# Title

bla bla bla

# Requirements

package:

# Run

```
python main.py --args~~~
```

# Ground rule

1. 기능을 구현할 때 값들은 최대한 코드에서 제외한다.
    - EX. 파일을 "10"개 읽는 코드를 작성하기 보단 파일을 "n"개 읽는 코드를 작성하고 n이 어떤 값인지는 사용할 때 정의하도록!
        - 이렇게 하는 목적은 언제 어디에서 각 값들이 사용되는지 파악하기 위한 것!
    - 다만 사실상 상수로 사용되는 값들은 default 값으로 지정해서 사용할 수 있도록
2. 내가 쓴 코드는 다른 사람이 모른다!
    - 파일을 읽는 코드를 구현했을 때, 해당 함수를 처음보면 뭔지 알 수 없다.
    - 그렇기 때문에 다음 정보들은 알려주면 도움이 된다.
        - 입/출력값은 (개념적으로) 무엇인지
        - 입/출력값의 자료형은 무엇인지
        - 미리보기도 있다면 좋다. 
            - ndarray나 tensor는 dimension과 같은 정보를 제공

## Naming Rule

- 파일명, 함수명과 변수명들은 snake case(ex. snake_case)로 하며 class는 camel case(ex. camelCase)로 정리
- Python Package로 구성할 경우 Package level에서 다루는 변수들은 snake/capital case(ex. CAPITAL_CASE)로 정리
- 변수명을 작성할 땐 큰 단위에서 작은 단위로 작성해보기(ex. 실수_정수_자연수)


# Description

## Data

raw: txt파일로 저장된 영화의 대본(4가지)
script: List[Str]로 저장된 영화의 문장들(TBD)

## Preprocess

## Model Architecture

## Visualization

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

np.random.seed(seed=1)

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['A', 'B', 'C']
)
df_map = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.title('Streamlit入門')
st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('こんにちは')

expander = st.expander('問い合わせ1')
expander.write('問い合わせ1の回答')
expander = st.expander('問い合わせ2')
expander.write('問い合わせ2の回答')
expander = st.expander('問い合わせ3')
expander.write('問い合わせ3の回答')

text = st.text_input('あなたの趣味を教えて下さい。')
condition = st.slider('VAS（痛みの評価）：', 0, 100, 0)

'あなたの趣味：', text
'VASの結果：', condition

# # selectBox
# option = st.selectbox(
#     'あなたが好きな数字を教えて下さい。',
#     list(range(1,11))
# )
# 'あなたの好きな数字は、', option, 'です。'

# 画像の表示
if st.checkbox('Show Image'):
    img = Image.open('cat.jpg')
    st.image(img, caption='マヌルネコ', use_column_width=True)

# st.write(df)
# 動的なテーブル
# st.dataframe(df.style.highlight_max(axis=0), width=400, height=400)
# 静的なテーブル
# st.table(df.style.highlight_max(axis=0))

# マジックコマンド
"""
### 使用するライブラリ
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

# 図
st.line_chart(df)
st.area_chart(df)
# 地図
# st.map(df_map)


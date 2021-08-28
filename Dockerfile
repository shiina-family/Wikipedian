# ライブラリビルド用ステージ
FROM python:3.9 as build_stage

# 作業用ディレクトリ
WORKDIR /opt

# venvを作る
RUN python -m venv /venv
# PATHの設定
ENV PATH="/venv/bin:$PATH"

# ライブラリの準備
COPY requirements.txt .
RUN pip3 install --upgrade -r  requirements.txt

# 実行ステージ
FROM python:3.9-slim
WORKDIR /opt
# これをしないとターミナルへの出力が出ない現象が起こる。
ENV PYTHONUNBUFFERED="1"
# venvをビルドステージから移植
COPY --from=build_stage /venv /venv
# PATHの設定
ENV PATH="/venv/bin:$PATH"

#　ソース追加
COPY . .

CMD ["python3", "bot.py"]
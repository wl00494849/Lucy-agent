### Lucy Agent介紹

Lucy-agent 是一個以 LINE Bot + LLM Agent 打造的智慧型個人助理系統，能主動協助管理日常任務，包括 Google 行事曆建立、時間提醒、資訊查詢、自然語言互動等。

1. 智慧型工作助理（LLM Agent）
	•	支援 RAG 搜尋與工具調用（Tool Calling），能理解自然語言指令並自動決定行動。
	•	自動幫使用者：
	•	建立 Google 行事曆事件
	•	安排提醒（如倒水、會議通知）
	•	提取並整理訊息內容

2. LineBot 互動介面
	•	使用 LINE Bot 作為主要入口，讓使用者能以聊天方式管理行程。
	•	例：
使用者：「星期三早上9點到11點要開會，30分鐘前通知我」
Lucy-agent 會自動解析 → 建立事件 → 設定提醒 → 回覆確認訊息。

3. 使用技術
	•	Backend：Golang、Python
	•	AI / LLM：OpenAI API、RAG、Tool Calling
	•	Infra：k3s、Docker、Nginx、Raspberry Pi
	•	Google Integration：Google Calendar API、Service Account
	•	Messaging：LINE Messaging API
    
### Lucy Agent 環境變數設定
Lucy Agent 建立時所需要的環境變數，主要分為兩個微服務。
一個是LineBot 一個是負責OpenAI Api的LLMs服務

Line Bot
1. LINE_CHANNEL_SECRET:
* 用途：用於驗證 LINE 平台送來的 Webhook 請求是否由官方發出。
* 來源：LINE Developers 後台 → Messaging API → Channel settings → Channel secret。

2. LINE_CHANNEL_TOKEN:
* 用途：用於讓伺服器透過 Messaging API 呼叫 LINE（例如推播訊息、回覆訊息）。
* 來源：LINE Developers 後台 → Messaging API → Channel access token。

Lucy Agent LLM

1. OPENAI_API_KEY:用於呼叫 OpenAI API（Chat Completions、Embeddings、Agents 等服務）。
2. GOOGLE_APPLICATION_CREDENTIALS:指定 Google Cloud Service Account 的金鑰檔案位置，用於 Google Cloud Client Libraries 的身份驗證。
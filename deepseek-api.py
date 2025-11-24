from openai import OpenAI

# 初始化客户端，配置API Key和基础URL
client = OpenAI(
    api_key="aikey",  # 请替换为你的真实API Key
    base_url="https://api.deepseek.com/v1"  # DeepSeek API的端点
)

def chat_with_deepseek():
    """
    一个简单的与DeepSeek模型对话的函数
    """
    print("欢迎使用DeepSeek对话助手！输入'退出'即可结束对话。")
    
    # 用于维护对话历史的列表
    messages = []
    
    while True:
        # 获取用户输入
        user_input = input("\n你: ")
        
        # 检查退出条件
        if user_input.lower() in ['退出', 'exit', 'quit']:
            print("再见！")
            break
        
        # 将用户输入添加到消息历史中
        messages.append({"role": "user", "content": user_input})
        
        try:
            # 调用DeepSeek API
            response = client.chat.completions.create(
                model="deepseek-chat",  # 指定使用的模型
                messages=messages,
                stream=False  # 如需流式输出（逐字显示），可设置为True
            )
            
            # 获取模型的回复
            assistant_reply = response.choices[0].message.content
            
            # 将模型的回复添加到消息历史中，以维持上下文
            messages.append({"role": "assistant", "content": assistant_reply})
            
            # 打印模型的回复
            print(f"\nDeepSeek: {assistant_reply}")
            
        except Exception as e:
            # 处理可能出现的错误
            print(f"\n抱歉，出错了: {e}")
            break

# 运行程序
if __name__ == "__main__":
    chat_with_deepseek()

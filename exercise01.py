# 网络标准化流程
# 分段寻址
# 在一个功能模块中功能尽可能单一 高内聚
# 模块之间尽量减少相互间的联系 低耦合
# 攻城狮 程序猿

# TCP
# 无丢失，无失序，无差错，无重复
"""
客户端向服务器发送消息报文请求连接
服务器受到请求，发送消息报文确认可以连接
客户端收到回复，发送最终报文连接建立
"""

from binance.client import Client

api_key = 'P0kxgPF1hlcx3dCYvAk03zJKM8OZNWWFkMHBuGLDlofKMqxvy5zt1FZKypOrNe1U'
api_secret = 'DQSLZyAKAJncDqze2oVxTaPCT0CoxdQZWP5aLLuFYGNzzAtSA47DKVWvYsxZHEkd'

client = Client(api_key, api_secret)

order = client.create_test_order(
    symbol='BNBBTC',
    side=Client.SIDE_BUY,
    type=Client.ORDER_TYPE_MARKET,
    quantity=100)
    





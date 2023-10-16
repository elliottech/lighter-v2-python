HOST = "https://api.lighter.xyz"
VERSION = "/v2"

# ------------ Blockchain IDs -----------
BLOCKCHAIN_ARBITRUM_GOERLI_ID = 421613
BLOCKCHAIN_ARBITRUM_ID = 42161

# ------------ Assets -------------------
TOKEN_USDC = "USDC"
TOKEN_WBTC = "WBTC"
TOKEN_WETH = "WETH"
TOKEN_LINK = "LINK"
TOKEN_UNI = "UNI"

# ------------ Orderbooks -------------------
ORDERBOOK_WETH_USDC = "WETH-USDC"
ORDERBOOK_WBTC_USDC = "WBTC-USDC"
ORDERBOOK_WETH_WBTC = "WETH-WBTC"
ORDERBOOK_UNI_USDC = "UNI-USDC"
ORDERBOOK_LINK_USDC = "LINK-USDC"
ORDERBOOK_USDT_USDC = "USDT-USDC"
ORDERBOOK_USDC_USDC = "USDC-USDC"

# ------------ Order Statuses -------------------
ORDER_STATUS_OPEN = "open"
ORDER_STATUS_FILLED = "filled"
ORDER_STATUS_CANCELLED = "canceled"

# ------------ Order Types -------------------
ORDER_TYPE_LIMIT = "limit"
ORDER_TYPE_MARKET = "market"


# ------------ Order Sides -------------------
ORDER_SIDE_SELL = "sell"
ORDER_SIDE_BUY = "buy"


# ------------ Candlestick Resolutions -------------------
CANDLESTICK_RESOLUTION_1MIN = "1min"
CANDLESTICK_RESOLUTION_5MIN = "5min"
CANDLESTICK_RESOLUTION_15MIN = "15min"
CANDLESTICK_RESOLUTION_1H = "1h"
CANDLESTICK_RESOLUTION_4H = "4h"
CANDLESTICK_RESOLUTION_1D = "1d"


# ------------ Ethereum Transactions ------------
DEFAULT_GAS_AMOUNT = 4000000
DEFAULT_GAS_MULTIPLIER = 1.2
DEFAULT_GAS_PRICE = 4000000000
DEFAULT_MAX_FEE_PER_GAS = 2000000000
DEFAULT_MAX_PRIORITY_FEE_PER_GAS = 0
MAX_SOLIDITY_UINT = (
    115792089237316195423570985008687907853269984665640564039457584007913129639935
)
DEFAULT_API_TIMEOUT = 3000

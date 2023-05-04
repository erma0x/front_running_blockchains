## Front running Attack
Front running on an exchange is a fraudulent practice in which a person gains unauthorized access to the order information of another trader or investor before the order is placed. Using this information, the subject profits from the advance knowledge of the order by buying or selling the same financial security before the original investor, in order to increase his gains or reduce his losses. This practice is considered illegal and can result in heavy penalties from financial regulators.


## Sandwitch Attack
For AMMs, arbitrage traders are financially incentivized to find assets that are trading at discounts in liquidity pools and buy them up until the asset’s price returns in line with its market price.

In essence, the price of an asset can substantially increase or decrease with a single big trade. That’s what sandwich attackers take benefit of, by sandwiching a big transaction by simultaneously front-running and back-running it.

    1. The attacker detects the victim’s transaction in the memepool.
    2. They front-run the victim’s transaction by attaching a higher transaction fee, thus ensuring the attacker’s transaction gets executed before the victim’s.
    3. Victims’ transactions get executed and suffer higher slippage by paying higher for an asset than they expected because of the attacker’s transaction resulting in an increase in the price of the asset.
    4. The attacker then back-runs the victim and makes a profit.
    5. Thus executing a sandwich attack – sandwiching the victim’s transaction with two transactions.

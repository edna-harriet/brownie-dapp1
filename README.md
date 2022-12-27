# brownie-dapp1

Brownie Framework (Python)

What is the Brownie Framework? Brownie is the most popular Python development framework for Ethereum. Brownie takes care of managing contract artifacts, allowing you to write simple, manageable contracts and deployment scripts for custom deployments,library linking and complex Ethereum applications.

Create a new folder for your project and open VC code on that folder.

Install Brownie - High-level framework for smart contracts development.

-$ sudo npm install ganache --global
 ganache

-$ pip install eth-brownie

-$ brownie -- version
-$ brownie init
-$ ls

-Explore folders that the Brownie scaffold has created: build, contracts, interfaces, scripts, tests, etc.
-Open the contract folder and create a new file called StoreValue.sol 
-Compile the code using Brownie by running:

-$ brownie compile

-Explore the json generated in the build folder.
-Add your Goerli account to Brownie. Get your private key from Metamask:

-$ brownie accounts new account1

-$ brownie accounts list

-Deploy a contract in your local
-Open the scripts folder and create a new file called deploy.py:
-Execute the code in your local environment (you are using Ganache behind the scenes):

-$ brownie run scripts/deploy.py

Test your contract
-Open the test folder and create a new file called test_store_value.py
Execute the testing script:

-$ brownie test -s

Deploy to the testnetHeader anchor link
-Add an environment variable for the infura key ID.

-For this, create .env and brownie-config.yaml files at the root folder in your project
    - .env file:
    
-$ export WEB3_INFURA_PROJECT_ID=<YOUR INFURA ID>
   - brownie-config.yaml file:
 
-dotenv: .env
-Deploy the contract in Goerli:
 
-$ brownie run scripts/deploy.py --network goerli










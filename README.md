# brownie-dapp1

# Brownie Framework (Python)

What is the Brownie Framework? Brownie is the most popular Python development framework for Ethereum. Brownie takes care of managing contract artifacts, allowing you to write simple, manageable contracts and deployment scripts for custom deployments,library linking and complex Ethereum applications.

Create a new folder for your project and open VC code on that folder.

Install Brownie - High-level framework for smart contracts development.

-$ sudo npm install ganache --global
 ganache

-$ pip install eth-brownie

-$ brownie --version

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

# Deploy a contract in your local
-Open the scripts folder and create a new file called deploy.py:
-Execute the code in your local environment (you are using Ganache behind the scenes):

-$ brownie run scripts/deploy.py

# Test your contract
-Open the test folder and create a new file called test_store_value.py
Execute the testing script:

-$ brownie test -s

# Deploy to the testnetHeader anchor link
-Add an environment variable for the infura key ID.

-For this, create .env and brownie-config.yaml files at the root folder in your project

    - .env file:
    
-$ export WEB3_INFURA_PROJECT_ID = YOUR INFURA ID
 
   - brownie-config.yaml file:
 
-dotenv: .env
 
# Deploy the contract in Goerli:
 
-$ brownie run scripts/deploy.py --network goerli

• Account shall be created to the brownie app before the deploy script.

• Incase you encounter FILENOTFOUNDERROR, while in the project folder, run:

-# $brownie accounts export account1 /home/harriet/.brownie/accounts/my-goerli-account.json



# React DApp

# React SPA and Dependacies

-Creat folder a folder for your project and initialise a react SPA app:

-$ npx create-react-app dapp

-$ cd dapp

-Test the installation of the react app:

-$ npm run start

-Install library dependancies: This DApp uses 2 libraries.

-Bootstrap: This lab will not focus on web development CSS and HTML, bootstrap is used to provde some basic visual formatting. Learn more 

-Web3: is a collection of libraries that allow interaction with a local or remote Ethereum node using HTTP, IPC or WebSocket. Learn more 

-$ npm install bootstrap react-bootstrap
-$ npm install web3

# Create React SPA Decentralized App (DApp)

-Add bootstrap source and clear out App.css. All code files are found in the dapp/scr/ folder unless otherwise specified

-Replace app.js file with the provided code.

-We will add all of the web3 components into this one page, but we will seperate them into a seperate folder and import them.

-Create components and contracts folders in the root of src folder.

-Add the StoreValue.json file, from build folder of the brownie project, to the contracts folder.

# Interacting with Provider (Wallet)

-Create a userCard.js file in the components folder, with the provided code:

-The userCard component is doing 3 things:

-Initialising the Web3 library with a static property from the Web3 library Web3.givenProvider. This initialises the web3 library with the current native provider for browser viewing the App In this example we are using the MetaMask as the provider. If the browser does not have a native provider, the Web3.givenProvider will return null.

-As an alternative to using the native provider, we could create a webSocket provider which we could initialize, in order to support browsers that do not have a native provider. We could also provide the option of using the native provider or falling back to the webSocket provider if none exists.

- Getting the Providers current connected network infromation web3.eth.net and selected the netowrk type property .getNetworkType, which provides the name of the connected netowrk. For this example the value returned should be goerli.

-Getting the Providers selected Address web3.currentProvider.selectedAddress, which is the address ID for the current selected account in the connected wallet. And making a request to the Ethereum network to read the ballance of the Providers selected address web3.eth.getBalance

-Update the App.js to import the userCard component:

-You will see that as well as importing the UserCard component, we have created two variables:

-The weiUnit variable, which we hand to the UserCard component in order to convert Eth to Wei.

-The account State variable, with its setAccount function which we hand to the UserCard component to hoist the users account object from the UserCard into the App These two variables are set in the App so we can use them both later in another component.

-Test the app to see the current state, interacting with the Provider.

-$ npm run start

# Interacting with Contracts

-Create a fundCard.js file in the components folder, with the following code:

-The fundCard component is doing 4 things:

-Importing the contract json file, that we copied into the contracts folder from our truffle project which is used for

-Instantiating a Contract class by reading form the Ethereum network, using the contract ABI fundContract.abi, which is the interface of the contract, and the contract address fundContract.networks[5777].address, which is the ID of the contract on the network, where networks[5777] is the goerli testnet.

-Once we have instantiated the Contract class, we can then interact directly with the contract on the Ethereum networking by calling its methods and properties, such as finding the owner of the contract by calling the owner method contract.methods.owner().call();.

-As with the userCard component, where we read the selected account balance, we can also read the balance of the contract by using the same web3.eth.getBalance function, however providing the contract address contract.options.address.

-Update the App.js to import the fundCard component:

# Contract transactions

Create a payForm.js file in the components folder, with the following code:

-The payForm component is doing 2 things:

-Using the weiUnit and gweiUnit variables to convert Eth into wei and gwei for a simple unit calculator, in order for the user to see the unit breakdowns, but also to use the wei value when we add a value to the contract.

-Using the account and contract variables we hoisted to the App from the userCard and fundCard, we call the fund method on the contract, and use the account as the sender of the funds.

-It is important to note, when we created the FundProjectForOwner in Solidity, we did not add paramaters to the fund method






















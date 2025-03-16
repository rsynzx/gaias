# **Gaianet Bot 🤖**  
just bot.

## Features 🌟
- Gaia Prompt Automatic Request
- Prompt Generator

## Prerequisites 📋
  
### Software Dependencies  
- Python (3.8 or higher)  
- Node.js (v14 or higher)  
- npm (Node Package Manager)  

## Installation 🚀

### 1. System Preparation  
```bash  
# Update system packages  
sudo apt update && sudo apt upgrade -y  

# Install essential tools  
sudo apt install git curl jq python3-pip nodejs npm -y  

# Install PM2 Process Manager  
sudo npm install -g pm2 
```

### 2. Clone Repository 

```bash  
git clone https://github.com/rsynzx/gaias.git gaias-bot
cd gaias-bot
````


## Usage 🛠️
Replace the domain with your specific domain in the 4th line of `run.sh`  
```bash
nano run.sh
```

## Run the bot 🕹️
1. Generate Keywords
```bash
python3 keywords.py
```
2. Make Script Executable
```bash
chmod +x run.sh
```
3. Run Bot [ Normal Version ]
```bash
./run.sh
```
## X. Run Bot [ Brutal Version ]
- Run :
```bash
for i in {1..50}; do pm2 start run.sh --name "gaia-chat-$i" --interpreter bash; done
```  
- Adjust `{1..50}` based on your computational resources  
- Potential ranges:  
  - Low-end: `{1..10}`  
  - Mid-range: `{1..100}`  
  - High-end: `{1..500}` 
  - Abnormal `{1..5000}` 

## X. Management Commands  
- List running instances
```bash  
pm2 list  
```
- View logs  
```bash 
pm2 logs
```
- Stop all instances  
```bash 
pm2 stop all  
```

## Contributing 📋
Feel free to submit issues and enhancement requests.

## License 📜 
This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer 🚨 
This tool is for educational purposes only. Use at your own risk and responsibility.

@Source-code :
- https://github.com/winsnip/gaiabot-winsnip
- https://github.com/Dwentzart/boted

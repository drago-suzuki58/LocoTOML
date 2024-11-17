import argparse
from locotoml import LocoTOML
import locale

# Get the system locale
system_locale = locale.getdefaultlocale()[0].split('_')[0] or "en"
if system_locale not in ["ja", "en"]:
    system_locale = "en"

loc = LocoTOML(locale=system_locale)

# コマンドライン引数のパーサーを作成
parser = argparse.ArgumentParser(
    description=loc.description()
    )

parser.add_argument("--lang", "-l", help=loc.help.lang(), default=system_locale)
parser.add_argument("--user", "-u", help=loc.help.user(), default="USER")

args = parser.parse_args()


loc.change_locale(args.lang)
print(loc.content.message(user=args.user))
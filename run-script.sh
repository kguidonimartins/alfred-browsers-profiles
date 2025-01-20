read browser profile <<< "{query}"

echo "Browser: $browser"
echo "Profile: $profile"

if [[ "$browser" == "CHROME_CANARY" ]]; then
	open -n -a "Google Chrome Canary" --args --profile-directory="$profile"

elif [[ "$browser" == "BRAVE" ]]; then
	open -n -a "Brave Browser" --args --profile-directory="$profile"

elif [[ "$browser" == "CHROME" ]]; then
	open -n -a "Google Chrome" --args --profile-directory="$profile"

elif [[ "$browser" == "FIREFOX" ]]; then
	/Applications/Firefox.app/Contents/MacOS/firefox -P --no-remote $profile

elif [[ "$browser" == "FIREFOX_DEV" ]]; then
	/Applications/FirefoxDeveloperEdition.app/Contents/MacOS/firefox -P --no-remote $profile

elif [[ "$browser" == "ORION" ]]; then
	open -n -a "$profile"

elif [[ "$browser" == "EDGE" ]]; then
	open -n -a "Microsoft Edge" --args --profile-directory="$profile"

elif [[ "$browser" == "EDGE_CANARY" ]]; then
	open -n -a "Microsoft Edge Canary" --args --profile-directory="$profile"
fi

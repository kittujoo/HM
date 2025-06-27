#!/bin/bash

set -e

# read properties file
propFile="$(dirname "$0")/allure.properties"
if [[ ! -f "$propFile" ]]; then
  echo "Error: $propFile does not exist."
  exit 1
fi

# Set variables from properties file
declare -A prop
while IFS='=' read -r key value; do
  if [ -n "$value" ]; then
    prop["$key"]="$value"
  fi
done < <(tr -d "\r" < "$propFile")

# Set the path to the Allure root directory
scriptDir="$(dirname "$(readlink -f "$0")")"
allureDir="$(dirname "$scriptDir")/.allure"


# Create the Allure root directory if it doesn't exist
if [[ ! -d "$allureDir" ]]; then
  mkdir -p "$allureDir"
fi

# Download the Allure CLI zip file if it doesn't exist
allurePath="$allureDir/allure-${prop[version]}/bin/allure"
if [[ ! -f "$allurePath" ]]; then
  echo "Downloading Allure CLI version ${prop[version]}..."
  allureUrl="${prop[commandLineUrl]}/${prop[version]}/allure-commandline-${prop[version]}.tgz"
  allureArchive="allure-${prop[version]}.tgz"

  curl -o "$allureDir/$allureArchive" "$allureUrl"
  tar zxf "$allureDir/$allureArchive" -C "$allureDir"

  rm "$allureDir/$allureArchive"
fi

# run allure command
"$allurePath" serve "${prop[allureResultsDirectory]}"

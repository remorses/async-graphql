set -x
cd `dirname $0`
cd ../src

git checkout master

# bump version
python -c '\
version = open("VERISON", "r").read().strip()
new = version.split(".")[-1]
new = int(new) + 1
new = str(new)
open("VERISON", "w").write(new)
'

# ssh-add -D
# ssh-keyscan github.com >> githubKey
# ssh-keygen -lf githubKey
# cat githubKey >> ~/.ssh/known_hosts


version=`cat VERSION`

git add VERSION
git commit -m "version $version"
git tag  "$version"
git push  https://${GITHUB_PERSONAL_TOKEN}@github.com/remorses/instagram-botnet.git --tags

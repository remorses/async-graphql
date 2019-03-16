set -x
cd `dirname $0`
cd ../src

git checkout master

# bump version
python -c '\
version = open("VERSION", "r").read().strip()
new = version.split(".")[-1]
new = int(new) + 1
new = ".".join(version.split(".")[:-1]) + "." + str(new)
open("VERSION", "w").write(new)
'

# ssh-add -D
# ssh-keyscan github.com >> githubKey
# ssh-keygen -lf githubKey
# cat githubKey >> ~/.ssh/known_hosts


version=`cat VERSION`

git config  user.email "beats.by.morse@gamil.com"
git config  user.name "Tommaso De Rossi"

git add VERSION
git commit -m "version $version"
git tag  -a "$version" -m "[skip ci]"
git push  --tags  https://${GITHUB_PERSONAL_TOKEN}@github.com/remorses/async-graphql.git HEAD

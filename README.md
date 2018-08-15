配置eslint:
frontend目录下：
npm install -g eslint

npm i eslint-plugin-vue@latest --save-dev

npm install --save-dev stylelint-config-standard

npm install -g --save-dev eslint-plugin-vue

npm install -g --save-dev eslint-plugin-import

npm install -g --save-dev eslint-plugin-node

npm install -g --save-dev eslint-plugin-promise

npm install -g --save-dev eslint-plugin-standard

npm install -g --save-dev babel-eslint

配置stylelint:
frontend目录下:
 npm install stylelint stylelint-order

 npm install --save-dev stylelint

 npm install --save-dev stylelint-config-standard

 npm install --save-dev stylelint-config-recess-order

 npm install -g stylelint

配置pylint:

pip install pylint

或者:

esay_install pylint

配置git hooks:

打开隐藏文件夹，进入.git/hooks

删除commit-msg.sample,pre-commit.sample

将shell script文件夹里面的脚本拷贝进去

即可在提交时自动检查代码风格

如果想取消掉自动检查的部分功能，直接在pre-commit脚本中注释掉相应代码即可

运行:

vagrant up

vagrant ssh

cd /vagrant

cd frontend

npm install

npm run build

cd ..

cd server

pip install Pillow

./manage.py makemigrations 

./manage.py migrate

./manage.py runserver 0:8000
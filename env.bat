echo@ 'Starting config frontend environment!'
copy .\shell_script\commit-msg .\.git\hooks
copy .\shell_script\pre-commit .\.git\hooks
del .\.git\hooks\commit-msg.sample
del .\.git\hooks\pre-commit.sample
call npm install -g eslint
call npm install --save-dev stylelint-config-standard
call npm install -g --save-dev eslint-plugin-vue
call npm install -g --save-dev eslint-plugin-import
call npm install -g --save-dev eslint-plugin-node
call npm install -g --save-dev eslint-plugin-promise
call npm install -g --save-dev eslint-plugin-standard
call npm install -g --save-dev babel-eslint
call npm install stylelint stylelint-order
call npm install --save-dev stylelint
call npm install --save-dev stylelint-config-standard
call npm install --save-dev stylelint-config-recess-order
call npm install -g stylelint
pip install pylint
pip install iview --save

echo@ 'Finsihing config frontend environment!'
pause
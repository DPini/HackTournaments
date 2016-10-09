oauth = OAuth(app)

github = oauth.remote_app(
    'github',
    consumer_key='a11a1bda412d928fb39a',
    consumer_secret='92b7cf30bc42c49d589a10372c3f9ff3bb310037',
    request_token_params={'scope': 'identity:basic,identity:avatar'},
    base_url='https://api.github.com/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://slack.com/oauth/authorize'
)

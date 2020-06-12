fake_db = {
    '/company/history': {
        'page_title': 'Company History',
        'page_details': 'Details about the company history ...'
    },
    '/company/employees': {
        'page_title': 'Our Team',
        'page_details': 'Details about the company employees ...'
    },
}


def get_page(url: str) -> dict:
    if not url:
        return {}

    url = url.strip().lower()
    url = '/' + url.lstrip('/')
    page = fake_db.get(url, {})

    return page

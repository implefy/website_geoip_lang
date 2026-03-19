{
    'name': 'Website GeoIP Language',
    'version': '19.0.1.0.0',
    'category': 'Website',
    'summary': 'Auto-switch website language based on visitor GeoIP country',
    'description': """
        Automatically selects the website language for first-time visitors
        based on their GeoIP-detected country:
        - Sweden (SE) -> Swedish (sv_SE)
        - Norway (NO) -> Norwegian Bokmal (nb_NO)
        - All other countries -> English (en_US)
    """,
    'author': 'implefy',
    'license': 'LGPL-3',
    'depends': ['website'],
    'installable': True,
    'application': False,
    'auto_install': False,
}

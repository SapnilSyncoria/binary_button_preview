{
    "name": "Binary Preview Button",
    "summary": "Adds a Preview button to the Binary field toolbar.",
    "version": "18.0.1.0.0",
    "category": "Tools",
    "author": "Sapnil Sarker Bipro",
    "license": "LGPL-3",
    "depends": ["web"],
    "assets": {
        "web.assets_backend": [
            "binary_preview_module/static/src/js/binary_preview_patch.js",
            "binary_preview_module/static/src/xml/binary_preview_patch.xml",
        ],
        "web.assets_backend_lazy": [
            "binary_preview_module/static/js/xml/binary_preview_patch.js",
            "binary_preview_module/static/src/xml/binary_preview_patch.xml",
        ],
    },
    "installable": True,
    "application": True,
'auto_install': False,
}
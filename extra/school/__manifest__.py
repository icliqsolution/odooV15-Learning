{
    'name':'School',
    'version' : '1.1',
    'author': 'weblearns',
    'summary' :'School management system',
    'sequence' : 1,
    'description' : "This is school management system software supported in"
                    "odoo v15",
    'category' : 'School',                
    'website' : 'https://freeweblearns.blogspot.com',
    'depends': ['base'],
    'data' : [
        "data/school_data.xml",
        "security/ir.model.access.csv",
        "views/school_view.xml",
        
    ],
    'demo':['demo/school_demo_data.xml']

}
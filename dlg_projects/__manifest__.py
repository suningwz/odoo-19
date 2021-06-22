# -*- coding: utf-8 -*-
{
    'name': "dlg_projects",

    'summary': """
        Módulo PROYECTOS para la gestión de proyectos y tareas""",

    'description': """
        Módulo PROYECTOS para la gestión de proyectos...
    """,

    'author': "DLG219",
    'website': "http://www.delegalog.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/phase.xml',
        'views/project.xml',
        'views/task.xml',
        'views/templates.xml',
        'reports/phase.xml',
        'reports/project.xml',
        'reports/task.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

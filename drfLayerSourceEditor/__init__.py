# -*- coding: utf-8 -*-
"""
/***************************************************************************
 drfLayerSourceEditor
                                 A QGIS plugin
 This plugin edits a layer's soure URI and reloads it
                             -------------------
        begin                : 2015-07-09
        copyright            : (C) 2015 by Dave Forrest
        email                : drf@vims.edu
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load drfLayerSourceEditor class from file drfLayerSourceEditor.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .layer_source_editor import drfLayerSourceEditor
    return drfLayerSourceEditor(iface)

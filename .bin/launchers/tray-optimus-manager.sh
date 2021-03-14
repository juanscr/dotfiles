#!/bin/bash

killall optimus-manager-qt
QT_STYLE_OVERRIDE=adwaita-dark QT_QPA_PLATFORMTHEME=gtk3 optimus-manager-qt

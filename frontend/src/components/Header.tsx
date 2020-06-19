import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';

export default function Header() {
    return (
        <AppBar position="relative">
            <Toolbar>
                <img src={"/images/logo.png"} alt="Classes.gg" />
            </Toolbar>
        </AppBar>
    )
}

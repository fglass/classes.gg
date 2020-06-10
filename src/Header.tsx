import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Logo from './logo.png';
import Toolbar from '@material-ui/core/Toolbar';


export default function Header() {
    return (
        <AppBar position="relative">
            <Toolbar>
                <img src={Logo} alt="Classes.gg" />
            </Toolbar>
        </AppBar>
    )
}

import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Logo from './logo.png';
import Toolbar from '@material-ui/core/Toolbar';
import {Link} from "react-router-dom";

export default function Header() {
    return (
        <AppBar position="relative">
            <Toolbar>
                <Link to="/">
                    <img src={Logo} alt="Classes.gg" />
                </Link>
            </Toolbar>
        </AppBar>
    )
}

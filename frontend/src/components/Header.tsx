import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import InputBase from "@material-ui/core/InputBase";
import SearchIcon from "@material-ui/icons/Search";
import Toolbar from '@material-ui/core/Toolbar';
import Typography from "@material-ui/core/Typography";
import { createStyles, fade, makeStyles, Theme } from "@material-ui/core/styles";

interface IProps {
    onSearch: (input: string) => void
}

const useStyles = makeStyles((theme: Theme) => createStyles({
    root: {
        flexGrow: 1,
    },
    title: {
        flexGrow: 1,
        display: 'block',
        paddingTop: theme.spacing(0.5),
        paddingLeft: theme.spacing(1),
        fontFamily: 'Bebas Neue',
        fontSize: '1.52rem',
    },
    search: {
        position: 'relative',
        borderRadius: theme.shape.borderRadius,
        backgroundColor: fade(theme.palette.common.white, 0.15),
        '&:hover': {
            backgroundColor: fade(theme.palette.common.white, 0.25),
        },
        marginLeft: theme.spacing(1),
        width: 'auto',
    },
    searchIcon: {
        padding: theme.spacing(0, 2),
        height: '100%',
        position: 'absolute',
        pointerEvents: 'none',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
    },
    inputRoot: {
        color: 'inherit',
    },
    inputInput: {
        padding: theme.spacing(1, 1, 1, 0),
        paddingLeft: `calc(1em + ${theme.spacing(4)}px)`,
        transition: theme.transitions.create('width'),
        width: '0ch',
        '&:focus': {
             width: '14ch',
        },
        [theme.breakpoints.up('sm')]: {
            width: '15ch',
            '&:focus': {
                 width: '22ch',
            },
        },
    },
}));


export default function Header(props: IProps) {
    const classes = useStyles()
    return (
        <div className={classes.root}>
            <AppBar position="static">
                <Toolbar>
                    <img src={"images/logo.svg"} alt="Logo" />
                    <Typography className={classes.title}>
                        Classes.gg
                    </Typography>
                    <div className={classes.search}>
                        <div className={classes.searchIcon}>
                            <SearchIcon />
                        </div>
                        <InputBase
                            placeholder="Search"
                            classes={{
                                root: classes.inputRoot,
                                input: classes.inputInput,
                            }}
                            onChange={(event) => props.onSearch(event.target.value.toLowerCase())}
                        />
                    </div>
                </Toolbar>
            </AppBar>
        </div>
    )
}

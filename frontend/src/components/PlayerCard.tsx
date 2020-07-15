import React from "react";
import Card from "@material-ui/core/Card";
import CardActionArea from "@material-ui/core/CardActionArea";
import CardMedia from "@material-ui/core/CardMedia";
import CardContent from "@material-ui/core/CardContent";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";

interface IProps {
    username: string,
    avatar: string,
    selectPlayer: (username: string) => void,
}

const useStyles = makeStyles((theme) => ({
    container: {
        margin: 'auto',
        maxWidth: 280,
        padding: theme.spacing(0, 0.5, 0, 0.5),
        [theme.breakpoints.down('sm')]: {
            padding: theme.spacing(0, 1.5, 0, 1.5),
        },
    },
    actionArea: {
        borderRadius: 16,
        transition: '0.2s',
        [theme.breakpoints.up('sm')]: {
            '&:hover': {
                transform: 'scale(0.9)',
            },
        },
    },
    card: {
        borderRadius: 16,
        boxShadow: 'none',
    },
    content: {
        backgroundColor: "#2196f3",
        padding: '1rem 1.5rem 1.5rem',
    },
    title: {
        fontFamily: 'Bebas Neue',
        fontSize: '2.25rem',
        [theme.breakpoints.down('md')]: {
            fontSize: '2rem',
        },
    },
    media: {
        backgroundColor: theme.palette.background.default,
        paddingTop: '70%',
    },
}));

export default function PlayerCard(props: IProps) {
    const { selectPlayer, avatar, username } = props
    const classes = useStyles()
    return (
        <div className={classes.container}>
            <CardActionArea
                classes={{root: classes.actionArea,}}
                onClick={_ => selectPlayer(username)}
            >
                <Card className={classes.card}>
                    <CardMedia
                        className={classes.media}
                        image={avatar}
                        title=""
                    />
                    <CardContent className={classes.content}>
                      <Typography className={classes.title} variant={'h2'}>
                          {username}
                      </Typography>
                    </CardContent>
                </Card>
            </CardActionArea>
        </div>
    );
};
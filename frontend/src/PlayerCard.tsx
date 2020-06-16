import React from "react";
import Card from "@material-ui/core/Card";
import CardActionArea from "@material-ui/core/CardActionArea";
import CardMedia from "@material-ui/core/CardMedia";
import CardContent from "@material-ui/core/CardContent";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";

interface IProps {
    avatar: string,
    username: string
}

const useStyles = makeStyles(() => ({
    actionArea: {
        maxWidth: 265,
        borderRadius: 16,
        transition: '0.2s',
        '&:hover': {
            transform: 'scale(0.9)',
        },
        "&:hover $focusHighlight": {
            opacity: 0
        },
    },
    focusHighlight: { },
    card: {
        borderRadius: 16,
        boxShadow: 'none',
    },
    content: {
        backgroundColor: "#2196f3",
        padding: '1rem 1.5rem 1.5rem',
    },
    title: {
        fontSize: '1.75rem',
        fontWeight: 450,
        color: '#fff',
        textTransform: 'uppercase',
    },
    media: {
        paddingTop: '70%',
    },
}));

const PlayerCard = ({ avatar, username }: IProps) => {
    const classes = useStyles()
    return (
        <CardActionArea
            classes={{
                root: classes.actionArea,
                focusHighlight: classes.focusHighlight
            }}
            href={`/player/${username}`}
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
    );
};

export default PlayerCard
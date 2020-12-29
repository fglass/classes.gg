export interface Player {
    username: string;
    avatar: string;
    lastUpdated: string;
    loadoutKeys: Array<String>;
}

export interface Loadout {
    game: string;
    source: string;
    attachments: { [type: string]: string };
}

export type LoadoutMap = { [loadout: string]: Loadout }
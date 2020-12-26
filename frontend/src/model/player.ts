export interface Player {
    username: string;
    avatar: string;
    lastUpdated: string;
    loadouts: { [loadout: string]: Loadout };
    nLoadouts: number;
}

export interface Loadout {
    game: string;
    source: string;
    attachments: { [type: string]: string };
}
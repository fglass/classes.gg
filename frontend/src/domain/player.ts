export interface Player {
    username: string;
    avatar: string;
    loadouts: { [key: string]: Loadout };
}

export interface Loadout {
    source: string;
    lastUpdated: string,
    attachments: Array<string>
}
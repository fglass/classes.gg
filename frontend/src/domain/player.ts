export interface Player {
    username: string;
    avatar: string;
    weapons: { [key: string]: Array<string> };
    commands: { [key: string]: string };
}
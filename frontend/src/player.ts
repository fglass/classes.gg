export interface Player {
    username: string;
    weapons: { [key: string]: Array<string> };
    commands: { [key: string]: string };
}
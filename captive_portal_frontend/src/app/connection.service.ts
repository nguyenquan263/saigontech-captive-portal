import { Injectable } from '@angular/core';

@Injectable()
export class ConnectionService {

  constructor() { }

  getConnection():string{

    return 'http://localhost:8080';
  }

}

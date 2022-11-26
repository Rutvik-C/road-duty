import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Home from '../components/home/Home';
import Challan from '../components/challan/Challan';

const AppRouter = () => (
  <BrowserRouter>
    <div className="container">
      <Switch>
        <Route component={Home} path="/" exact={true} />
        <Route component={Challan} path="/challan" />
      </Switch>
    </div>
  </BrowserRouter>
);

export default AppRouter;

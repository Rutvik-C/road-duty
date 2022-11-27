import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Home from '../components/home/Home';
import Challan from '../components/challan/Challan';
import Check from '../components/check/Check';
import Carousal from '../components/carousal/Carousal';

const AppRouter = () => (
  <BrowserRouter>
    <div className="container">
      <Switch>
        <Route component={Home} path="/" exact={true} />
        <Route component={Challan} path="/challan/:challanId" />
        <Route component={Check} path="/check" exact />
        <Route component={Carousal} path="/check/:challanId" />
      </Switch>
    </div>
  </BrowserRouter>
);

export default AppRouter;
